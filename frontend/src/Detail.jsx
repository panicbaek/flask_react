import { useEffect, useState } from "react"
import { useNavigate, useParams } from "react-router-dom"

const Detail = () => {

  const { id } = useParams() // 주소에 있는 id값을 꺼내줌
  const [post, setPost] = useState()
  const navigate = useNavigate()

  useEffect( () => {
    fetch(`http://localhost:5000/post/${id}`)
    .then(response => response.json())
    .then(data => {
      setPost(data.post)
    })
  }, [])

  if(!post)
    return <div>해당 게시글 없음</div>

  return (
    <>
      <h2>제목 : {post.title}</h2>
      <p>작성자 : {post.author.nickname}</p>
      <div>
        {post.content}
      </div>
      <button onClick={()=> {
        navigate(`/edit/${post.id}`, { state : {post : post} })
      }}>수정</button>
      <button onClick={ () => {
        fetch(`http://localhost:5000/post/${id}`, {
          method : 'DELETE',
          credentials : 'include'
        }).then(response => response.json())
        .then(data => {
          alert(data.message)

          if(data.ok)
          navigate('/')
        })

      }}>삭제</button>
    </>
  )
}

export default Detail