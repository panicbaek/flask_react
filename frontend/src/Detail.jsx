import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"

const Detail = () => {

  const { id } = useParams() // 주소에 있는 id값을 꺼내줌
  const [post, setPost] = useState()

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
      <button>수정</button>
      <button>삭제</button>
    </>
  )
}

export default Detail