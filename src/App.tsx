import styled from "styled-components";
import Authorization from "./components/authorization/Authorization";
import { ThemeProvider } from "styled-components";
import { baseTheme } from "./styles/theme";
import GlobalStyles from "./styles/global";
import { Route, Routes } from "react-router-dom";
import Chat from "./components/chat/Chat";
import Vacancies from "./components/vacancies/Vacancies";
import NotFound from "./components/NotFound";
import Zayavka from "./components/zayavka/Zayavka";
import Rf from "./components/zayavka/Rf";
import Vacancy from "./components/vacancy/Vacancy";
import Header from "./components/header/Header";
import * as C from "./styles/components";


function App() {
  return (
    <div>
      <ThemeProvider theme={baseTheme}>
        <Wrapper>
          <Header/>
          <C.Container>
            <Main>
              <Routes>
                <Route path="/" element={<Rf/>}/>
                <Route path="/authorization" element={<Authorization/>}/>
                <Route path="/vacancies" element={<Vacancies/>}/>
                <Route path="/vacancy" element={<Vacancy/>}/>
                <Route path="/zayavka" element={<Zayavka/>}/>
                <Route path="/chat" element={<Chat/>}/>
                <Route path="*" element={<NotFound />} />
              </Routes>
            </Main>
            <footer></footer>
            <GlobalStyles />
          </C.Container>
        </Wrapper>
      </ThemeProvider>
    </div>
  );
}

export default App;

const Wrapper = styled.div`
  width: 390px;
  margin: 0 auto;
`
const Main = styled.div`
  padding-top: 64px;
`