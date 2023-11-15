import React from 'react';
import Parcel from './components/Parcel';

const parcelsData = [
  { id: 1, trackingNumber: 'ABC123', delivered: false },
  { id: 2, trackingNumber: 'XYZ789', delivered: true },
  // Add more parcels as needed
];

const App: React.FC = () => {
  return (
    <div className="app">
      <h1>Parcel Tracking</h1>
      {parcelsData.map((parcel) => (
        <Parcel key={parcel.id} {...parcel} />
      ))}
    </div>
  );
};

export default App;