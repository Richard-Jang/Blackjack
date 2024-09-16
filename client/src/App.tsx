import { useState, useEffect } from 'react'
import viteLogo from './assets/icon.png'
import './App.css'
import axios from 'axios';

interface actor {
  hand: [],
  total: number,
}

function App() {
  const [player, setPlayer] = useState<actor>();
  const [dealer, setDealer] = useState<actor>();
  const [action, setAction] = useState<string>("");
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
      // const result = await response.json();
      // console.log(result);
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
          if (gameOver) setWinner(newData.winner);
        }
        setTriggerEffect(false);
      };
      updateGameState();
    }
    console.log(gameOver);
  }, [triggerEffect]);

  function handleHit() {
    setAction("hit");
    setTriggerEffect(true);
  }
  
  function handleStand() {
    setAction("stand");
    setTriggerEffect(true);
  }
  
  function handleAces() {
    setAction("aces");
    setTriggerEffect(true);
  }

  return (
    <>
      <div>
        <a href="https://www.ncpgambling.org/help-treatment/about-the-national-problem-gambling-helpline/" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
      </div>
      <div className="flex gap-4 w-full">
        <button className="btn" onClick={handleHit}>Hit</button>
        <button className="btn" onClick={handleStand}>Stand</button>
        <button className="btn" onClick={handleAces}>Aces</button>
      </div>
    </>
  )
}

export default App
