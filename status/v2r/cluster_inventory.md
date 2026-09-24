# V2R cluster inventory

2026-09-24T08:30:08.740294+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324401893376 available bytes; 81.90% used; 112490464 free inodes.

server1 `/home`: 324401893376 available bytes; 81.90% used; 112490464 free inodes.

server1 `/tmp`: 324401893376 available bytes; 81.90% used; 112490464 free inodes.

server1 `/var/tmp`: 324401893376 available bytes; 81.90% used; 112490464 free inodes.

server1 `/mnt/raid5`: 510113849344 available bytes; 97.66% used; 337721089 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57809104896 available bytes; 96.78% used; 110431002 free inodes.

server2 `/home`: 57809104896 available bytes; 96.78% used; 110431002 free inodes.

server2 `/tmp`: 57809104896 available bytes; 96.78% used; 110431002 free inodes.

server2 `/var/tmp`: 57809104896 available bytes; 96.78% used; 110431002 free inodes.

server2 `/mnt/raid5`: 516152537088 available bytes; 96.43% used; 445179646 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483024384 available bytes; 95.23% used; 114174984 free inodes.

server3 `/home`: 85483024384 available bytes; 95.23% used; 114174984 free inodes.

server3 `/data`: 175066230784 available bytes; 97.58% used; 225822976 free inodes.

server3 `/tmp`: 85483024384 available bytes; 95.23% used; 114174984 free inodes.

server3 `/var/tmp`: 85483024384 available bytes; 95.23% used; 114174984 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769254912 available bytes; 94.10% used; 114349119 free inodes.

server4 `/home`: 105769254912 available bytes; 94.10% used; 114349119 free inodes.

server4 `/data`: 275078434816 available bytes; 96.20% used; 225334672 free inodes.

server4 `/tmp`: 105769254912 available bytes; 94.10% used; 114349119 free inodes.

server4 `/var/tmp`: 105769254912 available bytes; 94.10% used; 114349119 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
