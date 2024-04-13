# Neural Networks From Scratch

This github repository represents the final deliverable for the 'Neural Networks from Scratch' project team lead by Nathan Kawamoto and Luke Yang for the MDST Winter 2024 semester.

## Releases

These zip files are for incorporating existing MLP models with frontend/backend. To install, download corresponding zip file for your model, following slides to incorporate your model and saved weights into the app.

[MNIST only](https://github.com/lukeyang01/nn-from-scratch/archive/refs/tags/MNIST_ONLY.zip)

[Credit Card only](https://github.com/lukeyang01/nn-from-scratch/archive/refs/tags/CC-ONLY.zip)

[NID only](https://github.com/lukeyang01/nn-from-scratch/archive/refs/tags/NID-ONLY.zip)

[Full web app (includes MNIST/CC/NID)](/releases/full_app.zip)

## Installation/Run Locally

Clone the project

```bash
  git clone https://github.com/lukeyang01/nn-from-scratch
```

Go to the project directory

```bash
  cd nn-from-scratch
```

Install dependencies

```bash
  ./install
```

Open two console windows:

Console 1 - Start the frontend

```bash
  npm run start
```

Console 2 - Start the backend (NOTE: Must cd into folder or dependencies/imports will not work)

```bash
  cd nn-backend
  ./run
```

## Screenshots

![MNIST](/screenshots/mnist_preview.png)

![Credit Card](/screenshots/credit_card_preview.png)

![Network Intrusion](/screenshots/nid_preview.png)

## Roadmap/TODO

- MNIST preprocessing for improved drawing accuracy

- Add support for training from frontend

- Overall styling overhaul
