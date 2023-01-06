import {Link} from `react-router-dom`
import styles from `./Navbar.module.css`

function Navbar()  {
    return (
        <ul className={styles.list}>
            <li className={styles.list}>
                <link to="/">HOME</link>
            </li>
            <li className={styles.itens}>
                <link to="/empresa">Empresa</link>
            </li>
            <li className={styles.itens}>
                <link to="/contato">contato</link>
            </li>
        </ul>
    )
} 

export default Navbar