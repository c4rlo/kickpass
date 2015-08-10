/*
 * Copyright (c) 2015 Paul Fariello <paul@fariello.eu>
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#ifndef KP_SAFE_H
#define KP_SAFE_H

#include "kickpass.h"

#ifndef KP_SAFE_TEMPLATE
#define KP_SAFE_TEMPLATE "%s\n"                                                \
                         "url: \n"                                             \
                         "username: \n"                                        \
                         "comment: \n"
#endif

#define KP_PLAIN_MAX_SIZE 4096

/*
 * A safe is either open or close.
 * Plain data are stored in memory.
 * Cipher data are stored in file.
 */
struct kp_safe {
	bool           open;            /* whether the safe is open or not */
	char           name[PATH_MAX];  /* name of the safe */
	int            cipher;          /* fd of the cipher file if the safe is open */
	size_t         plain_size;      /* size of the plaintext safe */
	unsigned char *plain;           /* data of the plaintext safe */
};

kp_error_t kp_safe_load(struct kp_ctx *, struct kp_safe *, const char *);
kp_error_t kp_safe_create(struct kp_ctx *, struct kp_safe *, const char *, const char *);
kp_error_t kp_safe_close(struct kp_ctx *, struct kp_safe *);
size_t     kp_safe_password_len(const struct kp_safe *);
kp_error_t kp_safe_get_path(struct kp_ctx *, struct kp_safe *, char *, size_t);
kp_error_t kp_safe_rename(struct kp_ctx *, struct kp_safe *, const char *);


#endif /* KP_SAFE_H */
