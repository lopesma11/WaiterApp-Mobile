import { Header } from "../components/Header";
import {
    Container,
    CategoriesContainer,
    MenuContainer,
    Footer,
    FooterContainer,
} from "./styles";

export function Main() {
    return (
        <>
            <Container>
                <Header />
                <CategoriesContainer />
                <MenuContainer />
            </Container>
            <Footer>
                <FooterContainer />
            </Footer>
        </>
    );
}
