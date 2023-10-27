    import './css/Colors.css'
    import logoWhite from '../assets/logo-white.png'



    export default function Colors() {

        return (
            <div className="colors">
                <div className='color' id="primary"><h1>primary</h1></div>
                <div className='color' id="complementary"><h1>complementary</h1></div>
                <div className='color' id="secondary"><h1>secondary</h1></div>
                <div className='color' id="dark"><h1>dark</h1></div>
                <div className='color' id="light"><h1>light</h1></div>
                <img src={logoWhite}></img>
            </div>
        )
    }