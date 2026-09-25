# V2R cluster inventory

2026-09-25T15:16:49.462743+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319043424256 available bytes; 82.20% used; 112476402 free inodes.

server1 `/home`: 319043424256 available bytes; 82.20% used; 112476402 free inodes.

server1 `/tmp`: 319043424256 available bytes; 82.20% used; 112476402 free inodes.

server1 `/var/tmp`: 319043424256 available bytes; 82.20% used; 112476402 free inodes.

server1 `/mnt/raid5`: 363950997504 available bytes; 98.33% used; 337545909 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23108960256 available bytes; 98.71% used; 110407934 free inodes.

server2 `/home`: 23108960256 available bytes; 98.71% used; 110407934 free inodes.

server2 `/tmp`: 23108960256 available bytes; 98.71% used; 110407934 free inodes.

server2 `/var/tmp`: 23108960256 available bytes; 98.71% used; 110407934 free inodes.

server2 `/mnt/raid5`: 320336166912 available bytes; 97.79% used; 445073317 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84425285632 available bytes; 95.29% used; 114153457 free inodes.

server3 `/home`: 84425285632 available bytes; 95.29% used; 114153457 free inodes.

server3 `/data`: 142178713600 available bytes; 98.04% used; 225807950 free inodes.

server3 `/tmp`: 84425285632 available bytes; 95.29% used; 114153457 free inodes.

server3 `/var/tmp`: 84425285632 available bytes; 95.29% used; 114153457 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638289408 available bytes; 94.10% used; 114349693 free inodes.

server4 `/home`: 105638289408 available bytes; 94.10% used; 114349693 free inodes.

server4 `/data`: 231346974720 available bytes; 96.80% used; 224944725 free inodes.

server4 `/tmp`: 105638289408 available bytes; 94.10% used; 114349693 free inodes.

server4 `/var/tmp`: 105638289408 available bytes; 94.10% used; 114349693 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
