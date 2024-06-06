import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './Main.css';

function Main() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    setPosts(storedPosts);
  }, []);

  return (
    <div className="container">
      <h1>Blog Posts</h1>
      <Link to="/create" className="create-link">Create New Post</Link>
      {posts.map((post, index) => (
        <div key={index} className="post">
          <h2>{post.title}</h2>
          <p>{post.content}</p>
          <div>
            {post.images.map((image, idx) => (
              <img key={idx} src={image} alt={`Post ${index} Image ${idx}`} />
            ))}
          </div>
          <Link to={`/post/${index}`}>Read more</Link>
        </div>
      ))}
    </div>
  );
}

export default Main;
