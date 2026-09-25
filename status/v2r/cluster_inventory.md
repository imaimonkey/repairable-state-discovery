# V2R cluster inventory

2026-09-25T14:56:52.790427+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319142989824 available bytes; 82.20% used; 112476961 free inodes.

server1 `/home`: 319142989824 available bytes; 82.20% used; 112476961 free inodes.

server1 `/tmp`: 319142989824 available bytes; 82.20% used; 112476961 free inodes.

server1 `/var/tmp`: 319142989824 available bytes; 82.20% used; 112476961 free inodes.

server1 `/mnt/raid5`: 364012457984 available bytes; 98.33% used; 337546353 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14379249664 available bytes; 99.20% used; 110407655 free inodes.

server2 `/home`: 14379249664 available bytes; 99.20% used; 110407655 free inodes.

server2 `/tmp`: 14379249664 available bytes; 99.20% used; 110407655 free inodes.

server2 `/var/tmp`: 14379249664 available bytes; 99.20% used; 110407655 free inodes.

server2 `/mnt/raid5`: 300290252800 available bytes; 97.93% used; 445074019 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84344938496 available bytes; 95.29% used; 114153954 free inodes.

server3 `/home`: 84344938496 available bytes; 95.29% used; 114153954 free inodes.

server3 `/data`: 142189150208 available bytes; 98.03% used; 225808253 free inodes.

server3 `/tmp`: 84344938496 available bytes; 95.29% used; 114153954 free inodes.

server3 `/var/tmp`: 84344938496 available bytes; 95.29% used; 114153954 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105645174784 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105645174784 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231417335808 available bytes; 96.80% used; 224945230 free inodes.

server4 `/tmp`: 105645174784 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105645174784 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
