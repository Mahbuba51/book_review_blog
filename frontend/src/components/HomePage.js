import React, { useEffect, useState } from 'react';
import axios from 'axios';

const HomePage = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
      console.log('Fetching books...');
    axios.get('/api/books/')
      .then(response => {
          console.log('Books fetched:', response.data);
        setBooks(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the books!', error);
      });
  }, []);

  return (
    <div>
      <h1>Book Reviews</h1>
      <ul>
        {books.map(book => (
          <li key={book.id}>
            <h2>{book.title}</h2>
            <p>Author: {book.author}</p>
            <p>Published: {book.publication_date}</p>
            {/* Add more details or a link to detailed review */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
