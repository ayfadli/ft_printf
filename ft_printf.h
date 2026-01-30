/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ayfadli <ayfadli@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 10:50:29 by ayfadli           #+#    #+#             */
/*   Updated: 2025/11/24 17:06:19 by ayfadli          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINT_H

# include "./utils/utils.h"
# include <stdarg.h>

int	ft_printf(const char *format, ...);
int	ft_check_format(const char format, va_list args);

#endif