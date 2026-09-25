# V2R cluster inventory

2026-09-25T14:15:36.038567+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319157460992 available bytes; 82.20% used; 112476975 free inodes.

server1 `/home`: 319157460992 available bytes; 82.20% used; 112476975 free inodes.

server1 `/tmp`: 319157460992 available bytes; 82.20% used; 112476975 free inodes.

server1 `/var/tmp`: 319157460992 available bytes; 82.20% used; 112476975 free inodes.

server1 `/mnt/raid5`: 364069281792 available bytes; 98.33% used; 337547424 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4722532352 available bytes; 99.74% used; 110407466 free inodes.

server2 `/home`: 4722532352 available bytes; 99.74% used; 110407466 free inodes.

server2 `/tmp`: 4722532352 available bytes; 99.74% used; 110407466 free inodes.

server2 `/var/tmp`: 4722532352 available bytes; 99.74% used; 110407466 free inodes.

server2 `/mnt/raid5`: 321854439424 available bytes; 97.78% used; 445075840 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281696256 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84281696256 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142213685248 available bytes; 98.03% used; 225808942 free inodes.

server3 `/tmp`: 84281696256 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84281696256 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654734848 available bytes; 94.10% used; 114349705 free inodes.

server4 `/home`: 105654734848 available bytes; 94.10% used; 114349705 free inodes.

server4 `/data`: 231451570176 available bytes; 96.80% used; 224947160 free inodes.

server4 `/tmp`: 105654734848 available bytes; 94.10% used; 114349705 free inodes.

server4 `/var/tmp`: 105654734848 available bytes; 94.10% used; 114349705 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
