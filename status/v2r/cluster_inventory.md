# V2R cluster inventory

2026-09-25T14:06:26.341097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319152164864 available bytes; 82.20% used; 112476968 free inodes.

server1 `/home`: 319152164864 available bytes; 82.20% used; 112476968 free inodes.

server1 `/tmp`: 319152164864 available bytes; 82.20% used; 112476968 free inodes.

server1 `/var/tmp`: 319152164864 available bytes; 82.20% used; 112476968 free inodes.

server1 `/mnt/raid5`: 364096643072 available bytes; 98.33% used; 337547470 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4732747776 available bytes; 99.74% used; 110407470 free inodes.

server2 `/home`: 4732747776 available bytes; 99.74% used; 110407470 free inodes.

server2 `/tmp`: 4732747776 available bytes; 99.74% used; 110407470 free inodes.

server2 `/var/tmp`: 4732747776 available bytes; 99.74% used; 110407470 free inodes.

server2 `/mnt/raid5`: 322112024576 available bytes; 97.77% used; 445076255 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281356288 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84281356288 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142223085568 available bytes; 98.03% used; 225809094 free inodes.

server3 `/tmp`: 84281356288 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84281356288 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654984704 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105654984704 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231486828544 available bytes; 96.80% used; 224948013 free inodes.

server4 `/tmp`: 105654984704 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105654984704 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
