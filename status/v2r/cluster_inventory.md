# V2R cluster inventory

2026-09-24T08:00:36.610686+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324412944384 available bytes; 81.90% used; 112490764 free inodes.

server1 `/home`: 324412944384 available bytes; 81.90% used; 112490764 free inodes.

server1 `/tmp`: 324412944384 available bytes; 81.90% used; 112490764 free inodes.

server1 `/var/tmp`: 324412944384 available bytes; 81.90% used; 112490764 free inodes.

server1 `/mnt/raid5`: 504141561856 available bytes; 97.69% used; 337722155 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57827422208 available bytes; 96.77% used; 110431072 free inodes.

server2 `/home`: 57827422208 available bytes; 96.77% used; 110431072 free inodes.

server2 `/tmp`: 57827422208 available bytes; 96.77% used; 110431072 free inodes.

server2 `/var/tmp`: 57827422208 available bytes; 96.77% used; 110431072 free inodes.

server2 `/mnt/raid5`: 517330092032 available bytes; 96.43% used; 445180561 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85484974080 available bytes; 95.23% used; 114175163 free inodes.

server3 `/home`: 85484974080 available bytes; 95.23% used; 114175163 free inodes.

server3 `/data`: 177834680320 available bytes; 97.54% used; 225838894 free inodes.

server3 `/tmp`: 85484974080 available bytes; 95.23% used; 114175163 free inodes.

server3 `/var/tmp`: 85484974080 available bytes; 95.23% used; 114175163 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779216384 available bytes; 94.10% used; 114349161 free inodes.

server4 `/home`: 105779216384 available bytes; 94.10% used; 114349161 free inodes.

server4 `/data`: 284236124160 available bytes; 96.07% used; 225366059 free inodes.

server4 `/tmp`: 105779216384 available bytes; 94.10% used; 114349161 free inodes.

server4 `/var/tmp`: 105779216384 available bytes; 94.10% used; 114349161 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
