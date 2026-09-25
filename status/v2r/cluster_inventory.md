# V2R cluster inventory

2026-09-25T13:51:10.487360+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319153889280 available bytes; 82.20% used; 112476962 free inodes.

server1 `/home`: 319153889280 available bytes; 82.20% used; 112476962 free inodes.

server1 `/tmp`: 319153889280 available bytes; 82.20% used; 112476962 free inodes.

server1 `/var/tmp`: 319153889280 available bytes; 82.20% used; 112476962 free inodes.

server1 `/mnt/raid5`: 364097839104 available bytes; 98.33% used; 337547544 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 7147999232 available bytes; 99.60% used; 110407605 free inodes.

server2 `/home`: 7147999232 available bytes; 99.60% used; 110407605 free inodes.

server2 `/tmp`: 7147999232 available bytes; 99.60% used; 110407605 free inodes.

server2 `/var/tmp`: 7147999232 available bytes; 99.60% used; 110407605 free inodes.

server2 `/mnt/raid5`: 322577940480 available bytes; 97.77% used; 445076691 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280786944 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84280786944 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142292819968 available bytes; 98.03% used; 225809361 free inodes.

server3 `/tmp`: 84280786944 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84280786944 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655377920 available bytes; 94.10% used; 114349713 free inodes.

server4 `/home`: 105655377920 available bytes; 94.10% used; 114349713 free inodes.

server4 `/data`: 231437873152 available bytes; 96.80% used; 224949646 free inodes.

server4 `/tmp`: 105655377920 available bytes; 94.10% used; 114349713 free inodes.

server4 `/var/tmp`: 105655377920 available bytes; 94.10% used; 114349713 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
