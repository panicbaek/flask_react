import { Link, Route, Routes } from 'react-router-dom'
import './App.css'
import Index from './Index'
import Singup from './Signup'

function App() {

  return (
    <>
    <header>
      <Link to='/'>인덱스</Link>
      <Link to='/signup'>회원가입</Link>
    </header>

    <Routes>
      <Route path='/' element={<Index/>}></Route>
      <Route path='/signup' element={<Singup/>}></Route>
    </Routes>

    </>
  )
}

export default App
