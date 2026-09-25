# V2R cluster inventory

2026-09-25T05:16:09.768380+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318890876928 available bytes; 82.21% used; 112480262 free inodes.

server1 `/home`: 318890876928 available bytes; 82.21% used; 112480262 free inodes.

server1 `/tmp`: 318890876928 available bytes; 82.21% used; 112480262 free inodes.

server1 `/var/tmp`: 318890876928 available bytes; 82.21% used; 112480262 free inodes.

server1 `/mnt/raid5`: 408539688960 available bytes; 98.13% used; 337570001 free inodes.
| server2 | True | ['5'] | [] | reference_compatible=False |

server2 `/`: 22930497536 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22930497536 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22930497536 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22930497536 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461608460288 available bytes; 96.81% used; 445108582 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84338548736 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84338548736 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142786936832 available bytes; 98.03% used; 225815145 free inodes.

server3 `/tmp`: 84338548736 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84338548736 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658884096 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658884096 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26301968384 available bytes; 99.64% used; 224960129 free inodes.

server4 `/tmp`: 105658884096 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658884096 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
