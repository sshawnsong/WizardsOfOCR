import React, { useState } from 'react';

const ListGroup = () => {
  const [selectedItem, setSelectedItem] = useState(null);

  const items = [
    'Item 1',
    'Item 2',
    'Item 3',
  ];

  return (
    <div>
      <h2>List Group Example</h2>
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            key={index}
            className={`list-group-item ${selectedItem === index ? 'active' : ''}`}
            onClick={() => setSelectedItem(index)}
          >
            {item}
          </li>
        ))}
      </ul>
      {selectedItem !== null && (
        <p>Selected Item: {items[selectedItem]}</p>
      )}
    </div>
  );
};

export default ListGroup;
