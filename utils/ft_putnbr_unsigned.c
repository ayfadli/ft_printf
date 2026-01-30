/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_unsigned.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ayfadli <ayfadli@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 10:50:51 by ayfadli           #+#    #+#             */
/*   Updated: 2025/11/17 17:53:52 by ayfadli          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

int	ft_putnbr_unsigned(unsigned int n)
{
	unsigned long	nb;
	int				count;

	count = 0;
	nb = n;
	if (nb >= 10)
		count += ft_putnbr_unsigned(nb / 10);
	count += ft_putchar(nb % 10 + 48);
	return (count);
}
