import { useState } from "react"
import { useLocation, useNavigate } from "react-router-dom"

const Edit = () => {

  const { state } = useLocation()
  const [post, setPost] = useState(state.post) // Detail컴포넌트에서 post정보를 보냄
  const navigate = useNavigate()

  const onChangeHandler = (e) => {
    setPost({
      ...post,
      [e.target.name] : e.target.value
    })
  }

  return (
    <>
      제목 : <input type="text" name="title" value={post.title} onChange={onChangeHandler}></input>
      내용 <br />
      <textarea name="content" value={post.content} onChange={onChangeHandler}></textarea>
      <br />
      <button onClick={ () => {
        fetch(`http://localhost:5000/post/${post.id}`, {
          method : 'PUT',
          headers : {
            'Content-Type' : 'application/json'
          },
          body : JSON.stringify(post),
          credentials : 'include'
        }).then(response => response.json())
        .then(data => {
          alert(data.message)

          if(data.ok)
            navigate(`/post/${post.id}`)
        })
        
      }}>수정</button>
    </>
  )
}

export default Edit