# V2R cluster inventory

2026-09-26T08:16:53.676158+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318746902528 available bytes; 82.22% used; 112475790 free inodes.

server1 `/home`: 318746902528 available bytes; 82.22% used; 112475790 free inodes.

server1 `/tmp`: 318746902528 available bytes; 82.22% used; 112475790 free inodes.

server1 `/var/tmp`: 318746902528 available bytes; 82.22% used; 112475790 free inodes.

server1 `/mnt/raid5`: 219140124672 available bytes; 98.99% used; 337539021 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22312112128 available bytes; 98.76% used; 110403905 free inodes.

server2 `/home`: 22312112128 available bytes; 98.76% used; 110403905 free inodes.

server2 `/tmp`: 22312112128 available bytes; 98.76% used; 110403905 free inodes.

server2 `/var/tmp`: 22312112128 available bytes; 98.76% used; 110403905 free inodes.

server2 `/mnt/raid5`: 255568990208 available bytes; 98.23% used; 445025295 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678206464 available bytes; 95.39% used; 114110813 free inodes.

server3 `/home`: 82678206464 available bytes; 95.39% used; 114110813 free inodes.

server3 `/data`: 123915972608 available bytes; 98.29% used; 225829156 free inodes.

server3 `/tmp`: 82678206464 available bytes; 95.39% used; 114110813 free inodes.

server3 `/var/tmp`: 82678206464 available bytes; 95.39% used; 114110813 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064535552 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064535552 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89381523456 available bytes; 98.76% used; 224883436 free inodes.

server4 `/tmp`: 106064535552 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064535552 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
