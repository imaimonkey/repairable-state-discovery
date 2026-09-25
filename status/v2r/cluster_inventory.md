# V2R cluster inventory

2026-09-25T15:06:07.975492+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319125606400 available bytes; 82.20% used; 112476952 free inodes.

server1 `/home`: 319125606400 available bytes; 82.20% used; 112476952 free inodes.

server1 `/tmp`: 319125606400 available bytes; 82.20% used; 112476952 free inodes.

server1 `/var/tmp`: 319125606400 available bytes; 82.20% used; 112476952 free inodes.

server1 `/mnt/raid5`: 364002328576 available bytes; 98.33% used; 337546009 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23110565888 available bytes; 98.71% used; 110407928 free inodes.

server2 `/home`: 23110565888 available bytes; 98.71% used; 110407928 free inodes.

server2 `/tmp`: 23110565888 available bytes; 98.71% used; 110407928 free inodes.

server2 `/var/tmp`: 23110565888 available bytes; 98.71% used; 110407928 free inodes.

server2 `/mnt/raid5`: 320637743104 available bytes; 97.78% used; 445073597 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84426969088 available bytes; 95.29% used; 114153452 free inodes.

server3 `/home`: 84426969088 available bytes; 95.29% used; 114153452 free inodes.

server3 `/data`: 142185758720 available bytes; 98.03% used; 225808109 free inodes.

server3 `/tmp`: 84426969088 available bytes; 95.29% used; 114153452 free inodes.

server3 `/var/tmp`: 84426969088 available bytes; 95.29% used; 114153452 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636458496 available bytes; 94.11% used; 114349691 free inodes.

server4 `/home`: 105636458496 available bytes; 94.11% used; 114349691 free inodes.

server4 `/data`: 231351123968 available bytes; 96.80% used; 224944880 free inodes.

server4 `/tmp`: 105636458496 available bytes; 94.11% used; 114349691 free inodes.

server4 `/var/tmp`: 105636458496 available bytes; 94.11% used; 114349691 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
