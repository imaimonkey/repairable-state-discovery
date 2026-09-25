# V2R cluster inventory

2026-09-25T14:59:58.692576+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319137140736 available bytes; 82.20% used; 112476957 free inodes.

server1 `/home`: 319137140736 available bytes; 82.20% used; 112476957 free inodes.

server1 `/tmp`: 319137140736 available bytes; 82.20% used; 112476957 free inodes.

server1 `/var/tmp`: 319137140736 available bytes; 82.20% used; 112476957 free inodes.

server1 `/mnt/raid5`: 366970654720 available bytes; 98.32% used; 337546325 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14378004480 available bytes; 99.20% used; 110407650 free inodes.

server2 `/home`: 14378004480 available bytes; 99.20% used; 110407650 free inodes.

server2 `/tmp`: 14378004480 available bytes; 99.20% used; 110407650 free inodes.

server2 `/var/tmp`: 14378004480 available bytes; 99.20% used; 110407650 free inodes.

server2 `/mnt/raid5`: 320311595008 available bytes; 97.79% used; 445073886 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84347113472 available bytes; 95.29% used; 114153954 free inodes.

server3 `/home`: 84347113472 available bytes; 95.29% used; 114153954 free inodes.

server3 `/data`: 142190157824 available bytes; 98.03% used; 225808207 free inodes.

server3 `/tmp`: 84347113472 available bytes; 95.29% used; 114153954 free inodes.

server3 `/var/tmp`: 84347113472 available bytes; 95.29% used; 114153954 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636724736 available bytes; 94.11% used; 114349709 free inodes.

server4 `/home`: 105636724736 available bytes; 94.11% used; 114349709 free inodes.

server4 `/data`: 231416848384 available bytes; 96.80% used; 224945089 free inodes.

server4 `/tmp`: 105636724736 available bytes; 94.11% used; 114349709 free inodes.

server4 `/var/tmp`: 105636724736 available bytes; 94.11% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
