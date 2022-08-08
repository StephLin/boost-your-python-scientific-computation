#if __INTELLISENSE__
#undef __ARM_NEON
#undef __ARM_NEON__
#endif

#include <pybind11/eigen.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

#include <omp.h>

namespace py = pybind11;

int omp_thread_count() {
  int n = 0;
  #pragma omp parallel reduction(+:n)
  n += 1;
  return n;
}

double arc_length(Eigen::Ref<Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> x) {
  double length = 0;
  omp_set_dynamic(0);     // Explicitly disable dynamic teams
  omp_set_num_threads(omp_thread_count()); // Use 4 threads for all consecutive parallel regions
  #pragma omp parallel for reduction(+:length)
  for (int i = 1; i < x.rows(); ++i) {
    length += (x.row(i) - x.row(i - 1)).norm();
  }
  return length;
}

PYBIND11_MODULE(lib, m) {
  m.def("arc_length", &arc_length);
}
