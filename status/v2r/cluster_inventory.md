# V2R cluster inventory

2026-09-25T13:29:46.176425+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319103336448 available bytes; 82.20% used; 112477545 free inodes.

server1 `/home`: 319103336448 available bytes; 82.20% used; 112477545 free inodes.

server1 `/tmp`: 319103336448 available bytes; 82.20% used; 112477545 free inodes.

server1 `/var/tmp`: 319103336448 available bytes; 82.20% used; 112477545 free inodes.

server1 `/mnt/raid5`: 370336755712 available bytes; 98.30% used; 337547839 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 15494418432 available bytes; 99.14% used; 110408608 free inodes.

server2 `/home`: 15494418432 available bytes; 99.14% used; 110408608 free inodes.

server2 `/tmp`: 15494418432 available bytes; 99.14% used; 110408608 free inodes.

server2 `/var/tmp`: 15494418432 available bytes; 99.14% used; 110408608 free inodes.

server2 `/mnt/raid5`: 323462688768 available bytes; 97.76% used; 445076926 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84202356736 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84202356736 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142349991936 available bytes; 98.03% used; 225809688 free inodes.

server3 `/tmp`: 84202356736 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84202356736 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655955456 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105655955456 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231396659200 available bytes; 96.80% used; 224951845 free inodes.

server4 `/tmp`: 105655955456 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105655955456 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
