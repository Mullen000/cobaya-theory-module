from scipy.stats import norm
from cobaya.likelihood import Likelihood
from cobaya.theory import Theory

class ACalculator(Theory):

    def initialize(self):
        pass
    def initialize_with_provider(self, provider):
        self.provider = provider
    
    def must_provide(self, **requirements):        
        
        #print('temp',temp)
        return {'H0':None}
    '''
    def get_can_provide_params(self):
        #print('15',['Aderived'])
        return ['Aderived']
    '''
    def calculate(self, state, want_derived=True, **params_values_dict):
        #print('1')
        H0 = self.provider.get_param('H0')
        #f = self.provider.get_param('H0_std')        
        state['A'] = H0/100
        #state['derived'] = {'Aderived': 10}
        
        #print('cal',state)
        
    def get_A(self, normalization=1):
        nom=self.current_state['A']# * normalization  
        #print('get A',nom)
        return nom
    
    


class TestLike(Likelihood):

    def initialize(self):
        
        #print('init',self.H0,self.H0_std)
        #print('H0',self.H0)
        self.norm = norm(loc=self.H0, scale=self.H0_std)
        #print('int2',self.norm)
        
        
    def get_requirements(self):
        return {'A':None,'H0':None}

    def logp(self, **params_values):
        H0_theory = self.provider.get_A()
        #print('h',H0_theory)
        return self.norm.logpdf(H0_theory*100)
