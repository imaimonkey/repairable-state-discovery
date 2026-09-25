# V2R cluster inventory

2026-09-25T15:12:14.335375+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319044882432 available bytes; 82.20% used; 112476402 free inodes.

server1 `/home`: 319044882432 available bytes; 82.20% used; 112476402 free inodes.

server1 `/tmp`: 319044882432 available bytes; 82.20% used; 112476402 free inodes.

server1 `/var/tmp`: 319044882432 available bytes; 82.20% used; 112476402 free inodes.

server1 `/mnt/raid5`: 353944707072 available bytes; 98.38% used; 337545963 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23109648384 available bytes; 98.71% used; 110407925 free inodes.

server2 `/home`: 23109648384 available bytes; 98.71% used; 110407925 free inodes.

server2 `/tmp`: 23109648384 available bytes; 98.71% used; 110407925 free inodes.

server2 `/var/tmp`: 23109648384 available bytes; 98.71% used; 110407925 free inodes.

server2 `/mnt/raid5`: 319931604992 available bytes; 97.79% used; 445073563 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84426543104 available bytes; 95.29% used; 114153450 free inodes.

server3 `/home`: 84426543104 available bytes; 95.29% used; 114153450 free inodes.

server3 `/data`: 142184599552 available bytes; 98.03% used; 225808018 free inodes.

server3 `/tmp`: 84426543104 available bytes; 95.29% used; 114153450 free inodes.

server3 `/var/tmp`: 84426543104 available bytes; 95.29% used; 114153450 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638432768 available bytes; 94.10% used; 114349692 free inodes.

server4 `/home`: 105638432768 available bytes; 94.10% used; 114349692 free inodes.

server4 `/data`: 231348957184 available bytes; 96.80% used; 224944782 free inodes.

server4 `/tmp`: 105638432768 available bytes; 94.10% used; 114349692 free inodes.

server4 `/var/tmp`: 105638432768 available bytes; 94.10% used; 114349692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
