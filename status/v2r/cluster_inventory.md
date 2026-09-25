# V2R cluster inventory

2026-09-25T14:21:42.531575+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319156174848 available bytes; 82.20% used; 112476975 free inodes.

server1 `/home`: 319156174848 available bytes; 82.20% used; 112476975 free inodes.

server1 `/tmp`: 319156174848 available bytes; 82.20% used; 112476975 free inodes.

server1 `/var/tmp`: 319156174848 available bytes; 82.20% used; 112476975 free inodes.

server1 `/mnt/raid5`: 364073144320 available bytes; 98.33% used; 337547392 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4721541120 available bytes; 99.74% used; 110407467 free inodes.

server2 `/home`: 4721541120 available bytes; 99.74% used; 110407467 free inodes.

server2 `/tmp`: 4721541120 available bytes; 99.74% used; 110407467 free inodes.

server2 `/var/tmp`: 4721541120 available bytes; 99.74% used; 110407467 free inodes.

server2 `/mnt/raid5`: 321680982016 available bytes; 97.78% used; 445075786 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84272758784 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84272758784 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142212100096 available bytes; 98.03% used; 225808849 free inodes.

server3 `/tmp`: 84272758784 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84272758784 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654599680 available bytes; 94.10% used; 114349712 free inodes.

server4 `/home`: 105654599680 available bytes; 94.10% used; 114349712 free inodes.

server4 `/data`: 231453237248 available bytes; 96.80% used; 224946788 free inodes.

server4 `/tmp`: 105654599680 available bytes; 94.10% used; 114349712 free inodes.

server4 `/var/tmp`: 105654599680 available bytes; 94.10% used; 114349712 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
