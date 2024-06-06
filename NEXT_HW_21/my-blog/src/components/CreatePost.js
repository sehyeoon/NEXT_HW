import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './CreatePost.css';

function CreatePost() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [images, setImages] = useState(['', '', '']);
  const navigate = useNavigate();

  const handleImageChange = (index, file) => {
    const reader = new FileReader();
    reader.onloadend = () => {
      const newImages = [...images];
      newImages[index] = reader.result;
      setImages(newImages);
    };
    reader.readAsDataURL(file);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const newPost = { title, content, images };
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    localStorage.setItem('posts', JSON.stringify([...storedPosts, newPost]));
    navigate('/');
  };

  return (
    <div className="container">
      <h1>Create a New Post</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </div>
        <div>
          <label>Content:</label>
          <textarea value={content} onChange={(e) => setContent(e.target.value)} required />
        </div>
        <div>
          <label>Image 1:</label>
          <input type="file" accept="image/*" onChange={(e) => handleImageChange(0, e.target.files[0])} />
        </div>
        <div>
          <label>Image 2:</label>
          <input type="file" accept="image/*" onChange={(e) => handleImageChange(1, e.target.files[0])} />
        </div>
        <div>
          <label>Image 3:</label>
          <input type="file" accept="image/*" onChange={(e) => handleImageChange(2, e.target.files[0])} />
        </div>
        <button type="submit">Create Post</button>
      </form>
    </div>
  );
}

export default CreatePost;
