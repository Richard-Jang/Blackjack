import { useEffect } from 'react'
import viteLogo from './assets/icon.png'
import './App.css'
import axios from 'axios';

function App() {
  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/users");
    console.log(response.data.users)
  };

  useEffect(() => {
    fetchAPI()
  }, [])

  return (
    <>
      <div>
        <a href="https://www.ncpgambling.org/help-treatment/about-the-national-problem-gambling-helpline/#:~:text=1%2D800%2DGAMBLER%20is%20the,the%20National%20Problem%20Gambling%20Helpline." target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
      </div>
      <h1></h1>
    </>
  )
}

export default App
