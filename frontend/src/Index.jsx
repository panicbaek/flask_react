import { useEffect, useState } from "react"
import { Link } from "react-router-dom"

const Index = () => {

  const [posts, setPosts] = useState()

  useEffect( () => {
    fetch('http://localhost:5000/post', {
      credentials:'include'
    }).then(response => response.json())
    .then(data => {
      setPosts(data.posts)
    })
  }, [])

  if(!posts)
    return <div>게시글 없음</div>
  
  return ( 
  <>
    <h2>인덱스 페이지</h2>

    <table>
      <thead>
      <tr>
        <th>번호</th>
        <th>제목</th>
        <th>작성자</th>
        <th>작성일</th>
      </tr>
      </thead>
      <tbody>
      {
        posts.map( (post) => {
          return (
            <tr key={post.id}>
              <td>{post.id}</td>
              <td>
                <Link to=''>{post.title}</Link>
              </td>
              <td>{post.author.nickname}</td>
              <td>{post.created_at}</td>
            </tr>
          )
        })
      }
      </tbody>
    </table>


  </>
  )
}

export default Index