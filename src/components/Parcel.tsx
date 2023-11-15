import React, { useState } from 'react';

interface ParcelProps {
  id: number;
  trackingNumber: string;
  delivered: boolean;
}

const Parcel: React.FC<ParcelProps> = ({ id, trackingNumber, delivered }) => {
  const [isDelivered, setIsDelivered] = useState(delivered);

  const handleDeliveryStatusToggle = () => {
    setIsDelivered(!isDelivered);
  };

  return (
    <div className="parcel">
      <p>Tracking Number: {trackingNumber}</p>
      <p>Status: {isDelivered ? 'Delivered' : 'In transit'}</p>
      <button onClick={handleDeliveryStatusToggle}>
        {isDelivered ? 'Mark as In Transit' : 'Mark as Delivered'}
      </button>
    </div>
  );
};

export default Parcel;