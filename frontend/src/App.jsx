import './App.css'

function App() {

  return (
    <>
      <button onClick={async ()=> {
        const response = await fetch('http://localhost:5000/check')
        const data = await response.josn()
        console.log(data)
      }}>체크</button>
    </>
  )
}

export default App
