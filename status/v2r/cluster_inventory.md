# V2R cluster inventory

2026-09-26T09:28:35.591408+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318628061184 available bytes; 82.22% used; 112475100 free inodes.

server1 `/home`: 318628061184 available bytes; 82.22% used; 112475100 free inodes.

server1 `/tmp`: 318628061184 available bytes; 82.22% used; 112475100 free inodes.

server1 `/var/tmp`: 318628061184 available bytes; 82.22% used; 112475100 free inodes.

server1 `/mnt/raid5`: 218973089792 available bytes; 99.00% used; 337538662 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22321332224 available bytes; 98.75% used; 110403908 free inodes.

server2 `/home`: 22321332224 available bytes; 98.75% used; 110403908 free inodes.

server2 `/tmp`: 22321332224 available bytes; 98.75% used; 110403908 free inodes.

server2 `/var/tmp`: 22321332224 available bytes; 98.75% used; 110403908 free inodes.

server2 `/mnt/raid5`: 254249508864 available bytes; 98.24% used; 445022871 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662047744 available bytes; 95.39% used; 114110799 free inodes.

server3 `/home`: 82662047744 available bytes; 95.39% used; 114110799 free inodes.

server3 `/data`: 123658600448 available bytes; 98.29% used; 225827858 free inodes.

server3 `/tmp`: 82662047744 available bytes; 95.39% used; 114110799 free inodes.

server3 `/var/tmp`: 82662047744 available bytes; 95.39% used; 114110799 free inodes.
| server4 | True | ['0', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106045591552 available bytes; 94.08% used; 114348131 free inodes.

server4 `/home`: 106045591552 available bytes; 94.08% used; 114348131 free inodes.

server4 `/data`: 89307422720 available bytes; 98.77% used; 224883085 free inodes.

server4 `/tmp`: 106045591552 available bytes; 94.08% used; 114348131 free inodes.

server4 `/var/tmp`: 106045591552 available bytes; 94.08% used; 114348131 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
