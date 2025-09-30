import { Link, Route, Routes } from 'react-router-dom'
import './App.css'
import Index from './Index'
import Singup from './Signup'
import Login from './Login'
import { useEffect, useState } from 'react'
import Write from './Write'
import Detail from './Detail'

function App() {

  const [userInfo, setUserInfo] = useState()

  useEffect(() => {
    fetch('http://localhost:5000/auth/me', {
      credentials:'include'
    }).then(response => response.json())
    .then(data => {
      setUserInfo(data.user)
    })

  }, [])

  return (
    <>
    {
      userInfo && <h4>{userInfo.nickname}님 반갑습니다.</h4>
    }

    <header>
      <Link to='/'>인덱스</Link>
      <Link to='/signup'>회원가입</Link>
      {
        userInfo
        ?<Link onClick={ () => {
          fetch('http://localhost:5000/auth/logout', {
            method: 'POST',
            credentials: 'include'
          }).then(response => response.json())
          .then(data => {
            setUserInfo(null)
          }).catch(e => {
            console.log(e)
          })
        }}>로그아웃</Link>
        :<Link to='/login'>로그인</Link> 
      }
      <Link to='/write'>게시글등록</Link>
    </header>

    <Routes>
      <Route path='/' element={<Index/>}></Route>
      <Route path='/signup' element={<Singup/>}></Route>
      <Route path='/login' element={<Login setUserInfo={setUserInfo} />}></Route>
      <Route path='/write' element={<Write/>}></Route>
      <Route path='/post/:id' element={<Detail/>}></Route>
    </Routes>

    </>
  )
}

export default App
