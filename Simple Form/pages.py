#Page Class to hold HTML Elements
class Page(object):
    #Initilization Function
    def __init__(self):
        #Main HTML Tempalte
        self.main_html = '''
<!DOCTYPE html>
<html lang="en">
    {head}
    {body}
</html>
        '''
        #Head HTML Template
        self.head_html = '''
<head>
    <title>Business Card Creator</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="css/style.css" >
    <link rel='stylesheet' type='text/css' href='https://fonts.googleapis.com/css?family=Signika:400,300,600'>
    {page_css}
</head>
        '''
        #Body HTML Tempalte
        self.body_html = '''
<body>
    <div class="wrapper">
        <header>
            <h1>Business Card Creator</h1>
            <p>Simple Form Assignment for DPW</p>
        </header>
        <main>
            <h2>{main_header}</h2>
            {main_content}
        </main>
    </div>
</body>
        '''

        #FORM PAGE ELEMENTS
        #Form CSS
        self.form_css = '''
        <link rel="stylesheet" type="text/css" href="/css/form.css" >
        '''
        #Header for form.
        self.main_header_form = "Please enter your information."
        #Form HTML Elements
        self.form_html = '''
            <form>
                <label for="fname">Name: </label>
                <fieldset>
                    <input type="text" name="fname" placeholder="James" id="fname" required>
                    <input type="text" name="lname" placeholder="Monroe" id="lname" required>
                </fieldset>
                <label for="job_title">Title:</label>
                <fieldset>
                    <input type="text" name="job_title" placeholder="President" id="job_title" value="">
                </fieldset>
                <label for="email">E-mail:</label>
                <fieldset>
                    <input type="email" name="email" placeholder="jmonroe@usa.gov" id="email" required>
                </fieldset>
                <label for="phone">Phone:</label>
                <fieldset>
                    <input type="tel" name="phone1" placeholder="680" id="phone" pattern="[0-9]{3}" oninvalid="this.setCustomValidity('Please enter the 3 digit area code')" oninput="setCustomValidity('')" required> - <input type="text" name="phone2" placeholder="222"
                    pattern="[0-9]{3}" oninvalid="this.setCustomValidity('Please enter the second 3 digits')" oninput="setCustomValidity('')" required> - <input type="text" name="phone3" placeholder="6135" pattern="[0-9]{4}" oninvalid="this.setCustomValidity('Please enter the final 4 digits.')"
                    oninput="setCustomValidity('')" required>
                </fieldset>
                <label>Phone Format:</label>
                <fieldset>
                    <label><input type="radio" name="phone_sep" value="classic" checked required>Classic <span>i.e. (680) 222-6135</span></label>
                    <label><input type="radio" name="phone_sep" value="dot">Dots <span>i.e. 680.222.6135</span></label>
                    <label><input type="radio" name="phone_sep" value="dash">Dash <span>i.e. 680-222-6134</span></label>
                </fieldset>

                <label for="address">Address:</label>
                <fieldset>
                    <input type="text" name="street" placeholder="1432 N Washington St." id="address"><br>
                    <input type="text" name="city" placeholder="Virginia">
                    <select name="state">
                        <option value="" disabled selected>State</option>
                        <option value="AL">Alabama</option>
                        <option value="AK">Alaska</option>
                        <option value="AZ">Arizona</option>
                        <option value="AR">Arkansas</option>
                        <option value="CA">California</option>
                        <option value="CO">Colorado</option>
                        <option value="CT">Connecticut</option>
                        <option value="DE">Delaware</option>
                        <option value="FL">Florida</option>
                        <option value="GA">Georgia</option>
                        <option value="HI">Hawaii</option>
                        <option value="ID">Idaho</option>
                        <option value="IL">Illinois</option>
                        <option value="IN">Indiana</option>
                        <option value="IA">Iowa</option>
                        <option value="KS">Kansas</option>
                        <option value="KY">Kentucky</option>
                        <option value="LA">Louisiana</option>
                        <option value="ME">Maine</option>
                        <option value="MD">Maryland</option>
                        <option value="MA">Massachusetts</option>
                        <option value="MI">Michigan</option>
                        <option value="MN">Minnesota</option>
                        <option value="MS">Mississippi</option>
                        <option value="MO">Missouri</option>
                        <option value="MT">Montana</option>
                        <option value="NE">Nebraska</option>
                        <option value="NV">Nevada</option>
                        <option value="NH">New Hampshire</option>
                        <option value="NJ">New Jersey</option>
                        <option value="NM">New Mexico</option>
                        <option value="NY">New York</option>
                        <option value="NC">North Carolina</option>
                        <option value="ND">North Dakota</option>
                        <option value="OH">Ohio</option>
                        <option value="OK">Oklahoma</option>
                        <option value="OR">Oregon</option>
                        <option value="PA">Pennsylvania</option>
                        <option value="RI">Rhode Island</option>
                        <option value="SC">South Carolina</option>
                        <option value="SD">South Dakota</option>
                        <option value="TN">Tennessee</option>
                        <option value="TX">Texas</option>
                        <option value="UT">Utah</option>
                        <option value="VT">Vermont</option>
                        <option value="VA">Virginia</option>
                        <option value="WA">Washington</option>
                        <option value="WV">West Virginia</option>
                        <option value="WI">Wisconsin</option>
                        <option value="WY">Wyoming</option>
                    </select>
                    <input type="text" name="zip_code" placeholder="20110" pattern="[0-9]{5}" oninvalid="this.setCustomValidity('Please enter a 5 digit zip code.')" oninput="setCustomValidity('')">
                </fieldset>
                <input type="submit" value="Create Card">
            </form>
        '''
        #Create the form page using the create_page function and store it.
        self.form_page = self.create_page(self.main_header_form, self.form_html, self.body_html, self.head_html, self.main_html, self.form_css)

        #CARD PAGE ELEMENTS
        #Card CSS
        self.card_css = '''
        <link rel="stylesheet" type="text/css" href="/css/card.css" >
        '''
        #Header for card.
        self.main_header_card = "Please see your card below"
        #Card Template
        self.card_html = '''
            <section>
                <h3>{name}</h3>
                <p>{title}</p>
                <section>
                    <p>{phone}</p>
                    <p>{email}</p>
                </section>
                <section>
                    <p>{street}</p>
                    <p>{city}</p>
                </section>
            </section>
        '''
        #Create the card page using the create_page function and store it.
        self.card_page = self.create_page(self.main_header_card, self.card_html, self.body_html, self.head_html, self.main_html, self.card_css)
    
    #CREATE PAGE FUNCTION
    def create_page(self, main_header, main_content, body, head, page, page_css):
        #Format the head using local variables.
        head = head.format(**locals())
        #Format the body using the local variables
        body = body.format(**locals())
        #Format the page using the local variables
        page = page.format(**locals())
        #Return the page.
        return page