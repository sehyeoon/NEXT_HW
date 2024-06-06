import React, { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import './Detail.css';

function Detail() {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const imageRefs = useRef([]);

  useEffect(() => {
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    setPost(storedPosts[id]);
  }, [id]);

  const handleImageClick = (idx) => {
    const newHref = prompt('Enter new image URL:');
    if (newHref) {
      imageRefs.current[idx].src = newHref;
    }
  };

  if (!post) return <div>Loading...</div>;

  return (
    <div className="container">
      <h1>{post.title}</h1>
      <p>{post.content}</p>
      <div>
        {post.images.map((image, idx) => (
          <img
            key={idx}
            src={image}
            alt={`Post Image ${idx}`}
            ref={(el) => (imageRefs.current[idx] = el)}
            onClick={() => handleImageClick(idx)}
          />
        ))}
      </div>
    </div>
  );
}

export default Detail;
