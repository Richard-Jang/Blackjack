import { useState, useEffect } from 'react'
import viteLogo from './assets/icon.png'
import './App.css'
import axios from 'axios';

interface actor {
  hand: [],
  paths: [],
  total: number,
}

function App() {
  const [player, setPlayer] = useState<actor>();
  const [dealer, setDealer] = useState<actor>();
  const [action, setAction] = useState<string>("");
  const [hasStand, setHasStand] = useState<boolean>(false);
  const [triggerEffect, setTriggerEffect] = useState<boolean>(false);
  const [gameOver, setGameOver] = useState<boolean>(false);
  const [winner, setWinner] = useState<string>("");

  const fetchAPI = async () => {
    try {
      const response = await axios.get("http://localhost:8080/api/data", {
        headers: {
          'Accept': 'application/json'
        }
      });
      return response.data;
    } catch (error) {
      console.error("Error fetching data: " + error);
    }
  };

  const sendAPI = async () => {
    try {
      const response = await fetch('http://localhost:8080/api/data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: {
          "player": player,
          "dealer": dealer,
          "action": action,
          "winner": "",
        }}),
      });
      console.log(response)
    } catch (error) {
      console.error("Error sending data: " + error);
    }
  }

  useEffect(() => {
    setAction("");
    setTriggerEffect(true);
    const initGame = async () => {
      const initialData = await fetchAPI();
      if (initialData) {
        setPlayer(initialData.player);
        setDealer(initialData.dealer);
      }
    };
    initGame();
  }, []);

  useEffect(() => {
    if (triggerEffect) {
      const updateGameState = async () => {
        await sendAPI();
        const newData = await fetchAPI();
        if (newData) {
          setPlayer(newData.player);
          setDealer(newData.dealer);
          setAction(newData.action);
          setGameOver((newData.winner == "player") || (newData.winner == "dealer"));
          setWinner(newData.winner);
        }
        setTriggerEffect(false);
      };
      updateGameState();
    }
  }, [triggerEffect]);

  function handleHit() {
    setAction("hit");
    setTriggerEffect(true);
  }
  
  function handleStand() {
    setAction("stand");
    setHasStand(true);
    setTriggerEffect(true);
  }
  
  function handleAces() {
    setAction("aces");
    setTriggerEffect(true);
  }

  return (
    <>
      <div className="w-screen h-screen flex">
        <div className="w-1/4 h-full bg-gray-700 font-serif flex flex-col justify-center items-center p-4">
          <div className="w-full">
            <h1 className="text-4xl text-white tracking-widest text-center">BLACKJACK</h1>
            <a href="https://www.ncpgambling.org/help-treatment/about-the-national-problem-gambling-helpline/#:~:text=1%2D800%2DGAMBLER%20is%20the,the%20National%20Problem%20Gambling%20Helpline." target="_blank" className='flex justify-center'>
              <img src={viteLogo} className="logo p-4" alt="Vite logo" />
            </a>
          </div>
          <div className="w-full flex-grow flex flex-col items-center justify-center gap-4">
            <button className={`w-9/12 h-fit text-3xl btn ${gameOver ? "btn-disabled" : ""}`} onClick={handleHit}>Hit</button>
            <button className={`w-9/12 h-fit text-3xl btn ${gameOver ? "btn-disabled" : ""}`} onClick={handleStand}>Stand</button>
            <button className={`w-9/12 h-fit text-3xl btn ${gameOver ? "btn-disabled" : ""}`} onClick={handleAces}>Aces</button>
          </div>
          <div className="w-full flex justify-center">
            <button className="w-8/12 h-fit btn text-2xl flex items-center justify-center bg-green-900 hover:bg-green-950 border-0">Gamble More</button>
          </div>
        </div>
        <div className="w-3/4 h-full flex flex-col items-center justify-between p-4 gap-3">
          <div className="w-full flex flex-col items-center justify-center gap-3">
            <h1 className="text-4xl font-serif">Dealer's Cards</h1>
            <div className="flex gap-2">
              {dealer?.paths.map((path, index) => {
                if (!gameOver && (index == dealer.paths.length - 1) && !hasStand) {
                  return <>
                  <div key={index}>
                    <img className="w-28 h-auto" src={"/Card_back_01.svg"} />
                  </div>
                </>
                } else {
                  return <>
                  <div key={index}>
                    <img className="w-28 h-auto" src={"/SVG-cards-1.3/" + path} />
                  </div>
                </>
                }
              })}
            </div>
          </div>
          <div className="w-10/12 h-3/6 rounded-full bg-[#583927] flex items-center justify-center px-8 py-4">
            <div className="w-full h-full rounded-full bg-[#d4af37] flex items-center justify-center px-8 py-4">
              <div className="w-full h-full rounded-full bg-green-900 flex items-center justify-center p-4">
                <div className={`w-11/12 h-5/6 rounded-full border border-4 flex ${gameOver ? "flex-col" : ""} items-center justify-center gap-3 p-8 font-serif`}>
                  {!gameOver ? (
                    <>
                      <div className="h-5/6 w-[15%] border border-4 rounded-lg"></div>
                      <div className="h-5/6 w-[15%] border border-4 rounded-lg"></div>
                      <div className="h-5/6 w-[15%] border border-4 rounded-lg"></div>
                      <div className="h-5/6 w-[15%] border border-4 rounded-lg"></div>
                      <div className="h-5/6 w-[15%] border border-4 rounded-lg"></div>
                    </>
                  ) : (
                    <>
                      <h1 className="text-7xl text-bold my-5">{winner.substring(0, 1).toUpperCase() + winner.substring(1)} wins!</h1>
                      <h3 className="text-2xl my-2">Player's total: {player?.total}</h3>
                      <h3 className="text-2xl my-2">Dealer's total: {dealer?.total}</h3>
                    </>
                  )}
                </div>
              </div>
            </div>
          </div>
          <div className="w-full flex flex-col items-center justify-center gap-3">
            <div className="flex gap-2">
              {player?.paths.map((path, index) => {
                return <>
                  <div key={index}>
                    <img className="w-28 h-auto" src={"/SVG-cards-1.3/" + path} />
                  </div>
                </>
              })}
            </div>
            <h1 className="text-4xl font-serif">
              Player's Cards
            </h1>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
