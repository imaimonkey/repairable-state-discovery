# V2R cluster inventory

2026-09-25T14:09:29.468995+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319151493120 available bytes; 82.20% used; 112476969 free inodes.

server1 `/home`: 319151493120 available bytes; 82.20% used; 112476969 free inodes.

server1 `/tmp`: 319151493120 available bytes; 82.20% used; 112476969 free inodes.

server1 `/var/tmp`: 319151493120 available bytes; 82.20% used; 112476969 free inodes.

server1 `/mnt/raid5`: 364983029760 available bytes; 98.33% used; 337547461 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4731453440 available bytes; 99.74% used; 110407468 free inodes.

server2 `/home`: 4731453440 available bytes; 99.74% used; 110407468 free inodes.

server2 `/tmp`: 4731453440 available bytes; 99.74% used; 110407468 free inodes.

server2 `/var/tmp`: 4731453440 available bytes; 99.74% used; 110407468 free inodes.

server2 `/mnt/raid5`: 322026786816 available bytes; 97.77% used; 445076155 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280946688 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84280946688 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142220349440 available bytes; 98.03% used; 225809044 free inodes.

server3 `/tmp`: 84280946688 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84280946688 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654882304 available bytes; 94.10% used; 114349706 free inodes.

server4 `/home`: 105654882304 available bytes; 94.10% used; 114349706 free inodes.

server4 `/data`: 231456993280 available bytes; 96.80% used; 224947689 free inodes.

server4 `/tmp`: 105654882304 available bytes; 94.10% used; 114349706 free inodes.

server4 `/var/tmp`: 105654882304 available bytes; 94.10% used; 114349706 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
