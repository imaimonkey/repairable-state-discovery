# V2R cluster inventory

2026-09-24T04:02:33.264277+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324721188864 available bytes; 81.88% used; 112493516 free inodes.

server1 `/home`: 324721188864 available bytes; 81.88% used; 112493516 free inodes.

server1 `/tmp`: 324721188864 available bytes; 81.88% used; 112493516 free inodes.

server1 `/var/tmp`: 324721188864 available bytes; 81.88% used; 112493516 free inodes.

server1 `/mnt/raid5`: 395987001344 available bytes; 98.18% used; 337724772 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40810594304 available bytes; 97.72% used; 110430856 free inodes.

server2 `/home`: 40810594304 available bytes; 97.72% used; 110430856 free inodes.

server2 `/tmp`: 40810594304 available bytes; 97.72% used; 110430856 free inodes.

server2 `/var/tmp`: 40810594304 available bytes; 97.72% used; 110430856 free inodes.

server2 `/mnt/raid5`: 525676003328 available bytes; 96.37% used; 445196813 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291978330112 available bytes; 83.71% used; 114176974 free inodes.

server3 `/home`: 291978330112 available bytes; 83.71% used; 114176974 free inodes.

server3 `/data`: 31754330112 available bytes; 99.56% used; 225842326 free inodes.

server3 `/tmp`: 291978330112 available bytes; 83.71% used; 114176974 free inodes.

server3 `/var/tmp`: 291978330112 available bytes; 83.71% used; 114176974 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791303680 available bytes; 94.10% used; 114349504 free inodes.

server4 `/home`: 105791303680 available bytes; 94.10% used; 114349504 free inodes.

server4 `/data`: 258333655040 available bytes; 96.43% used; 225381954 free inodes.

server4 `/tmp`: 105791303680 available bytes; 94.10% used; 114349504 free inodes.

server4 `/var/tmp`: 105791303680 available bytes; 94.10% used; 114349504 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
