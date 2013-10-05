def get_variables(env):
	if env.upper() == 'MACOS':
		return {'SHELL':'bash', 'VER':'LION'}
	elif env.upper() == 'WIN':
		return {'SHELL':'cmd', 'VER':'XP'}
	else:
		raise Exception('Unknown env %s' % env)