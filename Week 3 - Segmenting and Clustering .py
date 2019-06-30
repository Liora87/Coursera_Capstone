{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import urllib\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Use the BeautifulSoup package to scrape the web page, and find the table in this page. then take it out to save as a dataframe.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Postcode</th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighbourhood</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M1A</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>Not assigned</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M2A</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>Not assigned</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M3A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Parkwoods</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M4A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Victoria Village</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M5A</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Harbourfront</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Postcode           Borough     Neighbourhood\n",
       "0      M1A      Not assigned      Not assigned\n",
       "1      M2A      Not assigned      Not assigned\n",
       "2      M3A        North York         Parkwoods\n",
       "3      M4A        North York  Victoria Village\n",
       "4      M5A  Downtown Toronto      Harbourfront"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "URL = \"https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M\"\n",
    "page = urllib.request.urlopen(URL)\n",
    "soup = BeautifulSoup(page)\n",
    "page.close()\n",
    "table = soup.find_all('table')[0] \n",
    "df = pd.read_html(str(table))[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Ignore the cells which 'Borough' is 'Not assigned'**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[~df['Borough'].isin([\"Not assigned\"])]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Find the cells which 'Neighbourhood' is 'Not assigned', then change that to be the same with 'Borough'**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[df['Neighbourhood'] == 'Not assigned','Neighbourhood'] = df[df['Neighbourhood'] == 'Not assigned']['Borough']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Group the dataframe by 'Postcode'**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Postcode</th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighbourhood</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M1B</td>\n",
       "      <td>Scarborough</td>\n",
       "      <td>Rouge, Malvern</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M1C</td>\n",
       "      <td>Scarborough</td>\n",
       "      <td>Highland Creek, Rouge Hill, Port Union</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M1E</td>\n",
       "      <td>Scarborough</td>\n",
       "      <td>Guildwood, Morningside, West Hill</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M1G</td>\n",
       "      <td>Scarborough</td>\n",
       "      <td>Woburn</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M1H</td>\n",
       "      <td>Scarborough</td>\n",
       "      <td>Cedarbrae</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Postcode      Borough                           Neighbourhood\n",
       "0      M1B  Scarborough                          Rouge, Malvern\n",
       "1      M1C  Scarborough  Highland Creek, Rouge Hill, Port Union\n",
       "2      M1E  Scarborough       Guildwood, Morningside, West Hill\n",
       "3      M1G  Scarborough                                  Woburn\n",
       "4      M1H  Scarborough                               Cedarbrae"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "group = df.groupby('Postcode')\n",
    "group_ne = group['Neighbourhood'].apply(lambda x: \"%s\" % ', '.join(x))\n",
    "group_bo = group['Borough'].apply(lambda x: set(x).pop())\n",
    "df2 = pd.DataFrame(list(zip(group_bo.index, group_bo, group_ne)))\n",
    "df2.columns = ['Postcode', 'Borough', 'Neighbourhood']\n",
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The dataframe shape is (103, 3)\n"
     ]
    }
   ],
   "source": [
    "print('The dataframe shape is',df2.shape)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
