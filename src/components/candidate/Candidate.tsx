import React from 'react'
import { Link } from 'react-router-dom'
import Close from '../../images/icons/Close'
import * as C from '../../styles/components'
import * as S from './CandidateStyles'
import Telegram from '../../images/icons/Telegram'
import WatsApp from '../../images/icons/WatsApp'

const Candidate = () => {
    return (
        <div>
            <S.Title>
                <C.H2>Кандидат</C.H2>
                <Link to="/candidates">
                    <C.NButton>
                        <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
                    </C.NButton>
                </Link>
            </S.Title>
            <div>Прикреплен к вакансии ID888888 рекрутером 19.11.2023</div>
            <div>
                <div>ФИО</div>
                <S.ItemValue>Романова Валерия Тимуровна</S.ItemValue>
                <div>Вакансия</div>
                <S.ItemValue>Менеджер</S.ItemValue>
                <div>Заказчик</div>
                <S.ItemValue>Герасимов Андрей Антонович</S.ItemValue>
                <div>Реферер</div>
                <S.ItemValue>Иванов Иван Иванович</S.ItemValue>
                <div>Рекрутер</div>
                <S.ItemValue>Васильева Злата Ильинична</S.ItemValue>
                <div>Источник</div>
                <S.ItemValue>hh.ru</S.ItemValue>
                <div>Телефон</div>
                <S.ItemValue><a href="tel:+79999999999">+7 (646) 067-96-75</a></S.ItemValue>
                <S.MessengerWrapper>
                    <a href="https://t.me/+79999999999"><S.Messenger><Telegram/></S.Messenger></a>
                    <a href="https://wa.me/+79999999999"><S.Messenger><WatsApp/></S.Messenger></a>
                </S.MessengerWrapper>
                <C.LButton>Резюме</C.LButton>
                <S.Form>
                    <label htmlFor="">Статус</label>
                    <S.Select name="" id="">
                        <option value="0"></option>
                        <option value="1">Новый</option>
                        <option value="2">3-й недозвон</option>
                        <option value="3">Стажировка</option>
                    </S.Select>
                    <label htmlFor="">Комментарии</label>
                    <S.Textarea name="" id="" cols={30} rows={8}></S.Textarea>
                    <C.FButton>Cохранить</C.FButton>
                </S.Form>
            </div>
        </div>
    )
}

export default Candidate