import logo from './logo.svg';
import './App.css';

function App() {
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
          <form action="#" className="stkform">
            <h3>Make Payment</h3>
            <hr />
            <div>
              <input className='input-field text-center' type="tel" id='phone' name='phone' minLength='10' placeholder='Enter your Mpesa Number' required />
            </div>
            <div className='push'>
              <button>Pay</button>
            </div>
          </form>
        </div>
      </section>
    </>
  );
}

export default App;
