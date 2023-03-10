import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';

function App() {
  const [phone_number, setPhone] = useState('');
  const [message, setMessage] = useState('');
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  const axiosInstance = axios.create({
      baseURL: `https://payment.pythonanywhere.com`,
      headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json',
      }
  });


  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setSuccess(false);
    setLoading(true);
    console.log(phone_number)

    const body = JSON.stringify({phone_number})
    
    await axiosInstance({url:`/payment/pay/`, method: 'POST', data: body})
    .then((res) => {
      console.log(res.data)
      setSuccess(true);
      setMessage(res.data.success)
      setLoading(false);
      setPhone('')
    })
    .catch((error) => {
      console.log(error)
      setSuccess(false)
      if ('response' in error){
        setMessage(error.response.data.error)
      } else {
        setMessage(error.message)
      }
      
      setLoading(false)
    });

  };


  return (
    <>
      <nav>
        <div className='logo'>
          <a href="#">Payment Service</a>
        </div>
        <ul className='menu'>
          <li className='menu-item'><a href="#">Home</a></li>
          <li className='menu-item'><a href="#">About</a></li>
          <li className='menu-item'><a href="#">Contact</a></li>
        </ul>
      </nav>
      <section className='main'>
        <div className="box">
          <form onSubmit={handleSubmit} className="stkform">
            <h3>Make Payment</h3>
            <hr />
            <div>
              <input className='input-field text-center' type="tel" id='phone' name='phone' minLength='10' value={phone_number} onChange={e => setPhone(e.target.value)} placeholder='Enter your Mpesa Number' required />
            </div>
            <div className='push'>
              <button disabled={loading}>{loading ? <FontAwesomeIcon icon={faSpinner} spin /> : 'Pay'}</button>
            </div>
            <div>
              {success ? <p className='info'>{message}</p> : <p className='error'>{message}</p>}
            </div>
          </form>
        </div>
      </section>
    </>
  );
}

export default App;
