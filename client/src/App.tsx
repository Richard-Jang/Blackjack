import viteLogo from './assets/icon.png'
import './App.css'

function App() {

  return (
    <>

      <div className='fixed left-0 top-0 bg-gray-700 w-[25%] h-screen flex flex-col items-center justify-center space-y-4 font-serif'>
        <div className='fixed top-8 text-white font-serif md:text-3xl lg:text-4xl lg:tracking-widest'>
          BLACKJACK
        </div>

        <a href="https://www.ncpgambling.org/help-treatment/about-the-national-problem-gambling-helpline/#:~:text=1%2D800%2DGAMBLER%20is%20the,the%20National%20Problem%20Gambling%20Helpline." target="_blank" className='flex justify-center'>
          <img src={viteLogo} className="fixed top-20 logo" alt="Vite logo" />
        </a>

        <div className='flex flex-col space-y-16 '>
          <button className='btn lg:btn-wide font-light md:text-xl lg:text-2xl btn-xs sm:btn-sm md:btn-md lg:btn-lg'>
            Hit
          </button>

          <button className='btn lg:btn-wide font-light md:text-xl lg:text-2xl btn-xs sm:btn-sm md:btn-md lg:btn-lg'>
            Stand
          </button>
        </div>
      </div>

      <div className='fixed right-0 top-0 text-white w-[75%] h-screen flex justify-center items-center'>
        <div className='flex justify-center items-center w-[15rem] h-[7.5rem] md:w-[30rem] md:h-[15rem] lg:w-[60rem] lg:h-[30rem] rounded-full bg-[#583927]'>
          <div className='flex justify-center items-center w-[95%] h-[92.5%] rounded-full bg-[#d4af37]'>
            <div className='flex justify-center items-center w-[95%] h-[95%] rounded-full bg-green-900'>
              <div className='flex flex-row justify-center items-center w-[75%] h-[72.5%] rounded-full border-2 border-white space-x-1 md:space-x-3'>
                <div className='w-[1.25rem] md:w-[2.5rem] lg:w-[5rem] h-[50%] rounded-lg border-2 border-white'>
                </div>
                <div className='w-[1.25rem] md:w-[2.5rem] lg:w-[5rem] h-[50%] rounded-lg border-2 border-white'>
                </div>
                <div className='w-[1.25rem] md:w-[2.5rem] lg:w-[5rem] h-[50%] rounded-lg border-2 border-white'>
                </div>
                <div className='w-[1.25rem] md:w-[2.5rem] lg:w-[5rem] h-[50%] rounded-lg border-2 border-white'>
                </div>
                <div className='w-[1.25rem] md:w-[2.5rem] lg:w-[5rem] h-[50%] rounded-lg border-2 border-white'>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
