import React, { FC, useEffect } from 'react'
import * as C from '../../styles/components'
import * as S from './RegistrationStyles'
import { SubmitHandler, useForm } from 'react-hook-form'
import userApi from '../../services/AuthService'
import { useNavigate } from 'react-router-dom'
import { IRegQueryData } from '../../modules/IReg'

const Registration:FC = () => {

  const [registration, {data, error, isSuccess}] = userApi.useRegistrationMutation()

  if (data) {
    localStorage.setItem('accessToken', data.access)
    localStorage.setItem('role', data.user.role.toString())
  }

  const navigate = useNavigate()

  const goToAuth = () => navigate('/authorization')

  useEffect(() => {
    if (isSuccess) navigate('/vacancies')
  }, [isSuccess, navigate])

  const {
    register,
    formState: { errors, isValid},
    handleSubmit
  } = useForm<IRegQueryData>({mode: 'onBlur'})

  const onSubmit: SubmitHandler<IRegQueryData> = async (data) => {
    await registration(data)
  }

  return (
    <div>
        <S.Title>
            <C.H2>Зарегистрироваться</C.H2>
            <div onClick={goToAuth}>Войти</div>
      </S.Title>
      <S.Form onSubmit={handleSubmit(onSubmit)}>
        <S.Label htmlFor="firstName">Имя</S.Label>
        <S.Input id='firstName' {...register('firstName', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.firstName && <p>{errors?.firstName?.message}</p>}

        <S.Label htmlFor="nalastNameme">Фамилия</S.Label>
        <S.Input id='lastName' {...register('lastName', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.lastName && <p>{errors?.lastName?.message}</p>}

        <S.Label htmlFor="email">Email</S.Label>
        <S.Input id='email' {...register('email', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.email && <p>{errors?.email?.message}</p>}

        <S.Label htmlFor="phone">Телефон</S.Label>
        <S.Input id='phone' {...register('phone', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.phone && <p>{errors?.phone?.message}</p>}

        <S.Label htmlFor="role">Выберите свою роль</S.Label>
        <S.Select id='role' {...register('role', {required: 'Поле обязательно к заполнению'})}>
          <option value="1">Рекрутер</option>
          <option value="2">Рекрутер-администратор</option>
          <option value="3">Заказчик</option>
          <option value="4">Заказчик-руководитель</option>
        </S.Select>
        {errors?.role && <p>{errors?.role?.message}</p>}

        <S.Label htmlFor="username">Придумайте логин</S.Label>
        <S.Input id='username' {...register('username', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.username && <p>{errors?.username?.message}</p>}

        <S.Label htmlFor="password">Придумайте пароль</S.Label>
        <S.Input id='password' type="password" {...register('password', {required: 'Поле обязательно к заполнению'})} />
        {(errors?.password || error) && <p>{errors?.password?.message || 'Ошибка от апи'}</p>}
        <C.FButton disabled={!isValid}>Продолжить</C.FButton>
      </S.Form>
    </div>
  )
}

export default Registration

