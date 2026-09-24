# V2R cluster inventory

2026-09-24T09:07:30.567862+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324375318528 available bytes; 81.90% used; 112490085 free inodes.

server1 `/home`: 324375318528 available bytes; 81.90% used; 112490085 free inodes.

server1 `/tmp`: 324375318528 available bytes; 81.90% used; 112490085 free inodes.

server1 `/var/tmp`: 324375318528 available bytes; 81.90% used; 112490085 free inodes.

server1 `/mnt/raid5`: 503725207552 available bytes; 97.69% used; 337716071 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57786286080 available bytes; 96.78% used; 110430943 free inodes.

server2 `/home`: 57786286080 available bytes; 96.78% used; 110430943 free inodes.

server2 `/tmp`: 57786286080 available bytes; 96.78% used; 110430943 free inodes.

server2 `/var/tmp`: 57786286080 available bytes; 96.78% used; 110430943 free inodes.

server2 `/mnt/raid5`: 515286978560 available bytes; 96.44% used; 445178336 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85859028992 available bytes; 95.21% used; 114198464 free inodes.

server3 `/home`: 85859028992 available bytes; 95.21% used; 114198464 free inodes.

server3 `/data`: 167009648640 available bytes; 97.69% used; 225821711 free inodes.

server3 `/tmp`: 85859028992 available bytes; 95.21% used; 114198464 free inodes.

server3 `/var/tmp`: 85859028992 available bytes; 95.21% used; 114198464 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758871552 available bytes; 94.10% used; 114349076 free inodes.

server4 `/home`: 105758871552 available bytes; 94.10% used; 114349076 free inodes.

server4 `/data`: 318900031488 available bytes; 95.59% used; 225273384 free inodes.

server4 `/tmp`: 105758871552 available bytes; 94.10% used; 114349076 free inodes.

server4 `/var/tmp`: 105758871552 available bytes; 94.10% used; 114349076 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
