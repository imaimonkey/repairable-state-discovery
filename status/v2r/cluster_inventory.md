# V2R cluster inventory

2026-09-24T03:37:28.179247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324743282688 available bytes; 81.88% used; 112493812 free inodes.

server1 `/home`: 324743282688 available bytes; 81.88% used; 112493812 free inodes.

server1 `/tmp`: 324743282688 available bytes; 81.88% used; 112493812 free inodes.

server1 `/var/tmp`: 324743282688 available bytes; 81.88% used; 112493812 free inodes.

server1 `/mnt/raid5`: 397297225728 available bytes; 98.18% used; 337728033 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40829358080 available bytes; 97.72% used; 110431046 free inodes.

server2 `/home`: 40829358080 available bytes; 97.72% used; 110431046 free inodes.

server2 `/tmp`: 40829358080 available bytes; 97.72% used; 110431046 free inodes.

server2 `/var/tmp`: 40829358080 available bytes; 97.72% used; 110431046 free inodes.

server2 `/mnt/raid5`: 526994157568 available bytes; 96.36% used; 445197698 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291972780032 available bytes; 83.71% used; 114176120 free inodes.

server3 `/home`: 291972780032 available bytes; 83.71% used; 114176120 free inodes.

server3 `/data`: 36004368384 available bytes; 99.50% used; 225842875 free inodes.

server3 `/tmp`: 291972780032 available bytes; 83.71% used; 114176120 free inodes.

server3 `/var/tmp`: 291972780032 available bytes; 83.71% used; 114176120 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105793118208 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105793118208 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 279904366592 available bytes; 96.13% used; 225385031 free inodes.

server4 `/tmp`: 105793118208 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105793118208 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
