def calculate_probability(i, received_word, decoded_word, pi, pd, ps, D):
  """
  Calculate the probability of the i-th information bit given the received word and the current decoding information.

  Args:
    i: The index of the information bit.
    received_word: The received word from the channel.
    decoded_word: The currently decoded word.
    pi: The probability of insertion error.
    pd: The probability of deletion error.
    ps: The probability of substitution error.
    D: The maximum absolute value of drift.

  Returns:
    The probability of the i-th information bit being 0 and 1.
  """
  N = len(received_word)
  y = received_word
  u_hat = decoded_word

  # Initialize the probability of the i-th bit being 0 and 1
  W_i_0 = 0
  W_i_1 = 0

  # Iterate over all possible drift values
  for d in range(-D, D + 1):
    # Calculate the corresponding sequence y' given the drift d
    y_prime = [None] * (N + 1)
    for j in range(N):
      y_prime[j + d] = y[j]

    # Calculate the probability of y' given u_hat and drift d
    p_y_prime_u_hat_d = calculate_probability_y_prime_u_hat_d(y_prime, u_hat, d, pi, pd, ps)

    # Update W_i_0 and W_i_1 for drift d
    if d == 0:
      W_i_0 = p_y_prime_u_hat_d
    else:
      W_i_0 *= (1 - pi - pd) / 2
      W_i_1 *= (1 - pi - pd) / 2

    # Calculate the probability of y' given u_hat and drift d + 1
    p_y_prime_u_hat_d_plus_1 = calculate_probability_y_prime_u_hat_d(y_prime, u_hat, d + 1, pi, pd, ps)

    # Update W_i_0 and W_i_1 for drift d + 1
    if d + 1 <= D:
      W_i_0 += pi / 2 * p_y_prime_u_hat_d_plus_1
    if d - 1 >= -D:
      W_i_1 += pd / 2 * p_y_prime_u_hat_d_plus_1

  # Calculate the probability of the i-th bit being 0 and 1
  W_i_i = W_i_0 if u_hat[i] == 0 else W_i_1
  W_i_i_plus_1 = W_i_1 if u_hat[i] == 0 else W_i_0

  return W_i_i, W_i_i_plus_1

def calculate_probability(i, received_word, decoded_word, pi, pd, ps, D):
  """
  Calculate the probability of the i-th information bit given the received word and the current decoding information.

  Args:
    i: The index of the information bit.
    received_word: The received word from the channel.
    decoded_word: The currently decoded word.
    pi: The probability of insertion error.
    pd: The probability of deletion error.
    ps: The probability of substitution error.
    D: The maximum absolute value of drift.

  Returns:
    The probability of the i-th information bit being 0 and 1.
  """
  N = len(received_word)
  y = received_word
  u_hat = decoded_word

  # Initialize the probability of the i-th bit being 0 and 1
  W_i_0 = 0
  W_i_1 = 0

  # Iterate over all possible drift values
  for d in range(-D, D + 1):
    # Calculate the corresponding sequence y' given the drift d
    y_prime = [None] * (N + 1)
    for j in range(N):
      y_prime[j + d] = y[j]

    # Calculate the probability of y' given u_hat and drift d
    p_y_prime_u_hat_d = calculate_probability_y_prime_u_hat_d(y_prime, u_hat, d, pi, pd, ps)

    # Update W_i_0 and W_i_1 for drift d
    if d == 0:
      W_i_0 = p_y_prime_u_hat_d
    else:
      W_i_0 *= (1 - pi - pd) / 2
      W_i_1 *= (1 - pi - pd) / 2

    # Calculate the probability of y' given u_hat and drift d + 1
    p_y_prime_u_hat_d_plus_1 = calculate_probability_y_prime_u_hat_d(y_prime, u_hat, d + 1, pi, pd, ps)

    # Update W_i_0 and W_i_1 for drift d + 1
    if d + 1 <= D:
      W_i_0 += pi / 2 * p_y_prime_u_hat_d_plus_1
    if d - 1 >= -D:
      W_i_1 += pd / 2 * p_y_prime_u_hat_d_plus_1

  # Calculate the probability of the i-th bit being 0 and 1
  W_i_i = W_i_0 if u_hat[i] == 0 else W_i_1
  W_i_i_plus_1 = W_i_1 if u_hat[i] == 0 else W_i_0

  return W_i_i, W_i_i_plus_1

def calculate_probability_y_prime_u_hat_d(y_prime, u_hat, d, pi, pd, ps):
  """
  Calculate the probability of the received sequence y' given the decoded information u_hat and the drift d.

  Args:
    y_prime: The received sequence y' given the drift d.
    u_hat: The currently decoded word.
    d: The drift value.
    pi: The probability of insertion error.
    pd: The probability of deletion error.
    ps: The probability of substitution error.

  Returns:
    The probability of y' given u_hat and drift d.
  """
  # ... (Calculate the probability based on the IDS channel model and the given formulas) ...
  # ...

  return p_y_prime_u_hat_d
